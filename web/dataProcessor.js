var dataContainer = document.getElementById("networkData");

const splitLines = str => str.split(/\r?\n/);

function mergeDicts(dictOne, dictTwo) {
    var finalDict = {};
    for (var i in dictOne) {
      finalDict[i] = dictOne[i];
    }
    for (var j in dictTwo) {
        finalDict[j] = dictTwo[j];
    }
    return finalDict;
};

function readTextFile(file, alertUser) {
    var allText = "";
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function () {
        if(rawFile.readyState === 4) {
            if(rawFile.status === 200 || rawFile.status == 0) {
                allText = rawFile.responseText;
                if (alertUser === 1) {
                    alert(allText);
                }
                
            }
        }
    }
    rawFile.send(null);
    return allText;
};

function parseMassJSON(fileName) {
    ///console.log(readTextFile(fileName, 0))
    var counter = 0;
    var fullDict = {};
    var massJson = splitLines(readTextFile(fileName, 0)).slice(0, -1);
    console.log(massJson);
    for (line of massJson) {
        counter = counter + 1;
        var tempDict = [];
        tempDict[counter] = JSON.parse(line)
        fullDict = mergeDicts(fullDict, tempDict);
        //console.log(line);
        console.log(JSON.parse(line));
    }
    console.log('---\n')
    return fullDict;
};
console.log("---")
console.log(parseMassJSON("/network_log.json"));