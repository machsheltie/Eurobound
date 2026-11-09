-- Packs a PixelLab character export into one tagged .aseprite file for hand-fixing in Aseprite
-- and import into Godot through Aseprite Wizard (each tag becomes a SpriteFrames animation).
--
--   Aseprite.exe -b --script-param src=<character export dir> --script-param out=<file.aseprite>
--                --script-param fps=10 --script tools/sprite_pipeline/pack_aseprite.lua
--
-- Layout expected (PixelLab zip): <src>/<Animation>/rotations/<dir>.png for still poses and
-- <src>/<Animation>/<dir>/frame_NNN.png (or <dir>_NNN.png) for animated ones. Tags are named
-- "<animation>_<dir>" in snake_case, e.g. idle_south, walk_north_east.

local src = app.params["src"]
local out = app.params["out"]
local fps = tonumber(app.params["fps"] or "10")
assert(src and out, "pass --script-param src=... and out=...")
-- Hand edits in Aseprite are the master copy once they exist: never silently overwrite them.
assert(not app.fs.isFile(out) or app.params["force"] == "1",
  out .. " already exists (it may hold hand edits). Pass --script-param force=1 to overwrite.")

local DIRS = { "south", "south-east", "east", "north-east", "north", "north-west", "west", "south-west" }

local function snake(s)
  return (s:lower():gsub("[%s%-]+", "_"))
end

local function list_pngs(dir)
  local files = {}
  if not app.fs.isDirectory(dir) then return files end
  for _, f in ipairs(app.fs.listFiles(dir)) do
    if f:lower():match("%.png$") then table.insert(files, app.fs.joinPath(dir, f)) end
  end
  table.sort(files)
  return files
end

-- Collect {tag, frames[]} in a stable order.
local clips = {}
local anims = {}
for _, name in ipairs(app.fs.listFiles(src)) do
  if app.fs.isDirectory(app.fs.joinPath(src, name)) then table.insert(anims, name) end
end
table.sort(anims)
for _, anim in ipairs(anims) do
  local base = app.fs.joinPath(src, anim)
  for _, d in ipairs(DIRS) do
    local frames = list_pngs(app.fs.joinPath(base, d))
    if #frames == 0 then
      local still = app.fs.joinPath(base, "rotations", d .. ".png")
      if app.fs.isFile(still) then frames = { still } end
    end
    if #frames > 0 then
      table.insert(clips, { tag = snake(anim) .. "_" .. snake(d), frames = frames })
    end
  end
end
assert(#clips > 0, "no frames found under " .. src)

local first = Image { fromFile = clips[1].frames[1] }
local spr = Sprite(first.width, first.height, ColorMode.RGB)
spr.filename = out
local layer = spr.layers[1]
layer.name = "body"

-- All frames first, tags last: Aseprite stretches a tag over frames appended right after it,
-- so tagging while appending makes every tag swallow the rest of the timeline.
local frame_index = 1
local ranges = {}
for ci, clip in ipairs(clips) do
  local from = frame_index
  for fi, path in ipairs(clip.frames) do
    if not (ci == 1 and fi == 1) then spr:newEmptyFrame(frame_index) end
    local img = Image { fromFile = path }
    spr:newCel(layer, frame_index, img, Point(0, 0))
    spr.frames[frame_index].duration = 1.0 / fps
    frame_index = frame_index + 1
  end
  table.insert(ranges, { name = clip.tag, from = from, to = frame_index - 1 })
end
for _, r in ipairs(ranges) do
  local tag = spr:newTag(r.from, r.to)
  tag.name = r.name
end

spr:saveAs(out)
print(string.format("packed %d clips, %d frames -> %s", #clips, frame_index - 1, out))
