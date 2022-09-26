---
description: "Graphic for our Scrum Team using HTML, CSS, & JS"
title: "Scrum Team"
badges: true
comments: true
categories: [scrum]
layout: post
---


<html>

<body>

  <div style="display: flex; width: 100%; flex-direction: row; justify-content: center; align-items: center;">
    <svg height="300" viewBox="0 0 72 72" width="300" xmlns="http://www.w3.org/2000/svg"><g fill="none" fill-rule="evenodd"><path d="M36,72 L36,72 C55.882251,72 72,55.882251 72,36 L72,36 C72,16.117749 55.882251,-3.65231026e-15 36,0 L36,0 C16.117749,3.65231026e-15 -2.4348735e-15,16.117749 0,36 L0,36 C2.4348735e-15,55.882251 16.117749,72 36,72 Z" fill="#13cc5b"/><path d="M40.9273548,45.0723235 C40.9273548,43.4500009 42.0178065,41.7870332 42.8574194,40.9520654 C44.7967742,39.0243235 47.8033548,38.3577429 50.0492903,39.6909041 C50.7936774,40.1333558 51.1815484,40.4050977 51.7738065,40.9915493 C53.8594839,43.0563235 53.6643871,44.9074203 53.6643871,47.3809687 C53.6643871,47.7525816 53.4785806,47.938388 53.1069677,47.938388 L41.4847742,47.938388 C41.1131613,47.938388 40.9273548,47.7525816 40.9273548,47.3809687 L40.9273548,45.0723235 Z M28.1903226,33.6080654 L28.1903226,34.2456138 C28.1903226,36.6494848 30.5628387,39.0220009 32.9667097,39.0220009 L33.6030968,39.0220009 C36.008129,39.0220009 38.3794839,36.6494848 38.3794839,34.2456138 L38.3794839,33.6080654 C38.3794839,31.2053558 36.008129,28.8328396 33.6030968,28.8328396 L32.9667097,28.8328396 C30.5628387,28.8328396 28.1903226,31.2053558 28.1903226,33.6080654 Z M28.1903226,46.2661299 C28.1903226,47.2334848 28.0196129,47.938388 28.7477419,47.938388 L37.8232258,47.938388 C38.5501935,47.938388 38.3794839,47.2334848 38.3794839,46.2661299 C38.3794839,43.3373558 36.468,40.2959364 33.6030968,40.2959364 L32.9667097,40.2959364 C30.1087742,40.2959364 28.1903226,43.3408396 28.1903226,46.2661299 Z M18,36.1559364 C18,34.9156783 18.9522581,33.5952912 20.1205161,33.0227751 C21.5570323,32.3190332 23.4116129,32.6035493 24.5508387,33.7450977 C25.4659355,34.6590332 25.6424516,35.6078074 25.6424516,36.7934848 C25.6424516,39.6827751 21.5500645,41.6627751 19.0916129,39.2043235 C18.1788387,38.290388 18,37.3416138 18,36.1559364 Z M18,45.2314203 L18,47.3809687 C18,47.7525816 18.1858065,47.938388 18.5574194,47.938388 L25.0850323,47.938388 C25.4566452,47.938388 25.6424516,47.7525816 25.6424516,47.3809687 C25.6424516,45.5774848 25.8828387,44.1676783 24.5101935,42.7810977 C23.4336774,41.6952912 22.9563871,41.5687106 21.5024516,41.5687106 C19.6978065,41.5687106 18,43.7530977 18,45.2314203 Z M40.9273548,31.0613558 C40.9273548,33.1563235 41.4708387,34.5916783 42.7784516,35.8981299 C45.2589677,38.3798074 49.3327742,38.3798074 51.8144516,35.8981299 C54.296129,33.4164525 54.296129,29.3438074 51.8144516,26.8621299 C49.3350968,24.3827751 45.2636129,24.3758074 42.7784516,26.8621299 C41.8923871,27.7481945 40.9273548,29.3275493 40.9273548,31.0613558 Z" fill="#FFF"/></g></svg>
    <ul>
      <li>Scrum Master: Ethan Tran</li>
      <li>DevOPs: Rohin Sood</li>
      <li>Frontend Devs: Luna Iwazaki, Taiyo Iwazaki</li>
      <li>Backend Dev: Parav Salaniwal</li>
    </ul>
  </div>

  <div id="steps-container">
    
  </div>

</body>

<style>
  #steps-container {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    width: 100%;
    margin-top: 4px;
    gap: 4px;
    flex-grow: 4;
  }

  #step-box {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    padding-left: 6px;
    padding-right: 6px;
    border-radius: 8px;
    text-align: center;
  }

</style>

<script>
  var steps = ["Given Directions", "Assigning Jobs", "Determining Workload", "Planning Overview", "Deploy", "Finished Work"];

  var container = document.getElementById("steps-container");

  steps.forEach( (value, i) => {

    let num = document.createElement("h2");
    num.innerHTML = i + 1;

    let step = document.createElement("p");
    step.style.textAlign = "center";
    step.style.backgroundColor = "black";
    step.innerHTML = value;

    let box = document.createElement("div");
    box.setAttribute("id", "step-box");

    var randomColor = Math.floor(Math.random()*16777215).toString(16);

    box.style.backgroundColor = "#" + randomColor;

    box.appendChild(num);
    box.appendChild(step);

    container.appendChild(box);
 
  } );

</script>

</html>

 

