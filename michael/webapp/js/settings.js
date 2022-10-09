let modal = document.getElementById('settings')

function openModal() {
    modal.style.display = 'flex';
    setTimeout(function () {
        modal.style.opacity = '1';
    }, 20);
}

function closeModal() {
    modal.style.opacity = '0';
    setTimeout(function () {
        modal.style.display = 'none';
    }, 300);
}

function getValue(key, bool = false) {
    let value = localStorage.getItem(key)
    if (value == null || value == undefined) {
        if (bool) {
            return false;
        }
        return 3;
    }
    if (bool) {
        if (value == 'true') {
            return true;
        }
        return false;
    }
    return value;
}

let maxDocRange = document.getElementById("max-doc-range");
let maxAnsRange = document.getElementById("max-ans-range");
let maxDoc = document.getElementById("max-doc");
let maxAns = document.getElementById("max-ans");
let debugInfo = document.getElementById("debug-info");
// let evalMode = document.getElementById("eval-mode");


var value = getValue('max-doc')
maxDocRange.value = value;
maxDoc.innerText = value;

var value = getValue('max-ans')
maxAnsRange.value = value;
maxAns.innerText = value;

debugInfo.checked = getValue('debug-info', true)
// evalMode.checked = getValue('eval-mode', true)

maxDocRange.oninput = function () {
    maxDoc.innerText = this.value;
    localStorage.setItem('max-doc', this.value);
}

maxAnsRange.oninput = function () {
    maxAns.innerText = this.value;
    localStorage.setItem('max-ans', this.value);
}

debugInfo.onchange = function () {
    localStorage.setItem('debug-info', debugInfo.checked);
    if (debugInfo.checked) {
        debugInfoHeader.style.display = 'block'
        debugInfoSection.style.display = 'block'
        debugSection.style.display = 'block';
    } else {
        debugInfoHeader.style.display = 'none'
        debugInfoSection.style.display = 'none'
        debugSection.style.display = 'none';
    }

}

// evalMode.onchange = function () {
//     localStorage.setItem('eval-mode', evalMode.checked);
// }
