---
title: Lesson Progress
---

# 2D Array Visualization

<div style="margin: auto;"> 
  <canvas id="canvas"> </canvas>
</div>

<script>
const data = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];


function drawArray(data) {
  const canvas = document.getElementById('canvas');
  const context = canvas.getContext('2d');
  const cellWidth = 50;
  const cellHeight = 50;

  // Loop through the rows and columns of the 2D array
  for (let row = 0; row < data.length; row++) {
    for (let col = 0; col < data[row].length; col++) {
      const value = data[row][col]+100;
      const x = col * cellWidth;
      const y = row * cellHeight;

      // Draw a rectangle for each cell, with the value as the fill color
      context.fillStyle = `rgb(${value}, ${value}, ${value})`;
      context.fillRect(x, y, cellWidth, cellHeight);

      // Add a border around the rectangle
      context.strokeStyle = '#000';
      context.strokeRect(x, y, cellWidth, cellHeight);
    }
  }
}

drawArray(data);
</script>

# Dictionaries Visualization
<canvas id="canvas2" width="500" height="500" style="margin:auto"></canvas>
<script>
  const dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4"
  };
  const canvas = document.getElementById("canvas2");
  const ctx = canvas.getContext("2d");
  const dictKeys = Object.keys(dict);
  const dictValues = Object.values(dict);
  const dictEntries = Object.entries(dict);
  const dictSize = Object.keys(dict).length;
  const dictHeight = dictSize * 50;
  let y = 50;
  ctx.font = "16px Arial";
  ctx.fillStyle = "black";
  ctx.textAlign = "left";
  ctx.fillText("Dictionary", 10, y - 20);
  for (let i = 0; i < dictSize; i++) {
    ctx.fillStyle = "lightgray";
    ctx.fillRect(10, y, 200, 30);
    ctx.fillStyle = "black";
    ctx.fillText(dictKeys[i], 20, y + 20);
    ctx.fillText(dictValues[i], 120, y + 20);
    y += 50;
  }
  y = dictHeight + 50;
  ctx.fillText("Entries", 10, y - 20);
  for (let i = 0; i < dictSize; i++) {
    ctx.fillStyle = "lightgray";
    ctx.fillRect(10, y, 200, 30);
    ctx.fillStyle = "black";
    ctx.fillText(dictEntries[i][0], 20, y + 20);
    ctx.fillText(dictEntries[i][1], 120, y + 20);
    y += 50;
  }
</script>
