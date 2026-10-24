-- Normalize full-width Unicode digits in Pandoc textual nodes before LaTeX output.
-- This covers generated section labels and citation text from citeproc as well
-- as manuscript text; it deliberately leaves math and code unchanged.
local map = {
  ["０"]="0", ["１"]="1", ["２"]="2", ["３"]="3", ["４"]="4",
  ["５"]="5", ["６"]="6", ["７"]="7", ["８"]="8", ["９"]="9"
}
local function normalize(s)
  for full, ascii in pairs(map) do
    s = s:gsub(full, ascii)
  end
  return s
end
function Str(el)
  el.text = normalize(el.text)
  return el
end
