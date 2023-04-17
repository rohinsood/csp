---
title: Lesson Progress
layout: post
---

# 2D Array Visualization

<body>
  <div style="display: flex; flex-direction: column; justify-items: center;">
    <label for="rows">Rows (1-10):</label>
    <input type="number" id="rows" name="rows" min="1" max="10" value="3">
    <label for="cols">Columns (1-10):</label>
    <input type="number" id="cols" name="cols" min="1" max="10" value="3">
    <button onclick="generateArray()">Generate Array</button>
  </div>
  
  <table id="array">
  </table>
  
  <script>
  let data = [];
  
  function generateArray() {
    const rows = parseInt(document.getElementById('rows').value);
    const cols = parseInt(document.getElementById('cols').value);
  
    const newData = [];
    for (let row = 0; row < rows; row++) {
      const rowData = [];
      for (let col = 0; col < cols; col++) {
        if (row < data.length && col < data[row].length) {
          rowData.push(data[row][col]);
        } else {
          rowData.push(Math.floor(Math.random() * 256));
        }
      }
      newData.push(rowData);
    }
  
    data = newData;
    drawArray(data);
  }
  
  function drawArray(data) {

    const table = document.getElementById('array');
    table.innerHTML = '';
  
    // Loop through the rows and columns of the 2D array
    for (let row = 0; row < data.length; row++) {
      const tr = document.createElement('tr');
      for (let col = 0; col < data[row].length; col++) {
        const value = data[row][col];
        const td = document.createElement('td');
        td.textContent = value;
        td.style.backgroundColor = `rgb(${value}, ${value}, ${value})`;
        td.style.width = "50px"
        td.style.height = "50px"
        td.addEventListener('click', function() {
          data[row][col] = Math.floor(Math.random() * 256);
          drawArray(data);
        });

        const p = document.createElement('p')
        p.textContent = "(" + row + ", " + col + ")"
        p.style.color = "black"
        p.setAttribute("class", "coordinate")

        td.appendChild(p)

        tr.appendChild(td);

      }

      table.appendChild(tr);
    }
  }
  
  generateArray();
  </script>

  <style>
    .coordinate {
      opacity: 0;
    }

    .coordinate:hover {
      opacity: 100;
    }
  </style>
        
</body>

# Dictionaries Visualization
<body>
  <table>
    <caption>Dictionary</caption>
    <thead>
      <tr>
        <th>Key</th>
        <th>Value</th>
      </tr>
    </thead>
    <tbody id="dict-table">
      <tr>
        <td>key1</td>
        <td>value1</td>
      </tr>
      <tr>
        <td>key2</td>
        <td>value2</td>
      </tr>
      <tr>
        <td>key3</td>
        <td>value3</td>
      </tr>
      <tr>
        <td>key4</td>
        <td>value4</td>
      </tr>
    </tbody>
  </table>
  
  <script>
    let dict = {
      "key1": "value1",
      "key2": "value2",
      "key3": "value3",
      "key4": "value4"
    };
    let dictTable = document.getElementById("dict-table");
    let dictKeys = Object.keys(dict);
    let dictValues = Object.values(dict);
    let dictSize = Object.keys(dict).length;
  
    // Function to update the dictionary table with the current dictionary object
    function updateDictTable() {
      // Clear the current table rows
      dictTable.innerHTML = "";
      
      // Add a new row for each key-value pair in the dictionary object
      for (let i = 0; i < dictSize; i++) {
        const row = document.createElement("tr");
        const keyCell = document.createElement("td");
        const valueCell = document.createElement("td");
        keyCell.textContent = dictKeys[i];
        valueCell.textContent = dictValues[i];
        row.appendChild(keyCell);
        row.appendChild(valueCell);
        dictTable.appendChild(row);
      }
    }
  
    // Function to add a new key-value pair to the dictionary object and table
    function addDictPair() {
      const keyInput = document.getElementById("key-input");
      const valueInput = document.getElementById("value-input");
      const newKey = keyInput.value;
      const newValue = valueInput.value;
      if (newKey && newValue && !dict.hasOwnProperty(newKey)) {
        dict[newKey] = newValue;
        dictKeys.push(newKey);
        dictValues.push(newValue);
        dictSize++;
        updateDictTable();
        keyInput.value = "";
        valueInput.value = "";
      }
    }
  
    // Function to remove a key-value pair from the dictionary object and table
    function removeDictPair(key) {
      const index = dictKeys.indexOf(key);
      if (index > -1) {
        dictKeys.splice(index, 1);
        dictValues.splice(index, 1);
        dictSize--;
        delete dict[key];
        updateDictTable();
      }
    }
  
    updateDictTable();
  </script>
  
  <!-- Form to add new key-value pairs -->
  <form>
    <label for="key-input">Key:</label>
    <input id="key-input" type="text" name="key">
    <label for="value-input">Value:</label>
    <input id="value-input" type="text" name="value">
    <button type="button" onclick="addDictPair()">Add</button>
  </form>
</body>
