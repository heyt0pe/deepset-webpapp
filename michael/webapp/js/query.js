let query = document.getElementById('query-text')
let debugSection = document.getElementById('debug-section')

let loadingSection = document.getElementsByClassName('loading')[0]
let resultsSection = document.getElementsByClassName('results')[0]


let answersDiv = document.getElementById('answers')

let debugInfoHeader = document.getElementById('debug-info-header')
let debugInfoSection = document.getElementById('debug-info-section')

let loading = false;

// query.value = 'What are some ways to increase checkout conversion rate?'
// window.onload = function () {
//     LFQAQuery();
// }

async function LFQAQuery() {
    try {
        if (query.value.trim().length > 1) {
            setLoading(true)
            const request = await fetch('http://127.0.0.1:5000/lfqa-query', {
                method: "POST",
                body: JSON.stringify({
                    'query': query.value,
                    'max-doc': parseInt(getValue('max-doc')),
                    'max-ans': parseInt(getValue('max-ans'))
                })
            })
            const response = await request.json()
            if (response.error == false) {
                for (answer of response.answers) {
                    if (answer.answer.length > 1) {
                        let ansSec = '';
                        if (answer.type == 'extractive') {
                            ansSec = `
                            <p class="res">
                                <span>...${cleanExtractiveAnswer(answer.context, answer.answer)}...</span>
                            </p>
                            <p class="res">
                                <span class="bold">Relevance: </span> 
                                <span>${Math.round(answer.score * 100) / 100}</span>
                            </p>
                            <p class="res">
                                <span class="bold">Source: </span> 
                                <span>${answer.meta.name} - </span>
                                <span class="bold">Page Number: </span> 
                                <span>${answer.meta.page}</span>
                            </p>
                            `
                        } else {
                            ansSec = `
                            <p class="res">
                                <span>${cleanAnswer(answer.answer)}</span>
                            </p>
                            <p class="res">
                                <span class="bold">Sources: ${getDocuments(answer.meta.titles)}</span>
                            </p>`
                        }
                        let node = document.createElement("section");
                        node.classList.add('response')
                        node.innerHTML = ansSec
                        answersDiv.appendChild(node);
                    }
                }
                let debugInfo = getValue('debug-info');
                if (debugInfo == 'false') {
                    debugInfo = false;
                } else {
                    debugInfo = true;
                }
                if (!debugInfo) {
                    debugSection.innerText = JSON.stringify(response, null, 4)
                    debugInfoHeader.style.display = 'none'
                    debugInfoSection.style.display = 'none'
                    debugSection.style.display = 'none';
                } else {
                    debugSection.innerText = JSON.stringify(response, null, 4)
                    debugInfoHeader.style.display = 'block'
                    debugInfoSection.style.display = 'block'
                    debugSection.style.display = 'block';
                }
            } else {
                showNotification(response.msg, 'error')
            }
            setLoading(false)
        } else {
            showNotification('Enter a valid search term', 'error')
        }
    } catch (e) {
        console.log(e)
        setLoading(false)
        resultsSection.style.display = 'none';
        showNotification(e.message + '. Ensure the server is running', 'error')
    }
}

async function RAGQuery() {
    try {
        if (query.value.trim().length > 1) {
            setLoading(true)
            const request = await fetch('http://127.0.0.1:5000/rag-query', {
                method: "POST",
                body: JSON.stringify({
                    'query': query.value,
                    'max-doc': parseInt(getValue('max-doc')),
                    'max-ans': parseInt(getValue('max-ans'))
                })
            })
            const response = await request.json()
            if (response.error == false) {
                for (answer of response.answers) {
                    if (answer.answer.length > 1) {
                        let ansSec = '';
                        if (answer.type == 'extractive') {
                            ansSec = `
                            <p class="res">
                                <span>...${cleanExtractiveAnswer(answer.context, answer.answer)}...</span>
                            </p>
                            <p class="res">
                                <span class="bold">Relevance: </span> 
                                <span>${Math.round(answer.score * 100) / 100}</span>
                            </p>
                            <p class="res">
                                <span class="bold">Source: </span> 
                                <span>${answer.meta.name} - </span>
                                <span class="bold">Page Number: </span> 
                                <span>${answer.meta.page}</span>
                            </p>
                            `
                        } else {
                            ansSec = `
                            <p class="res">
                                <span>${cleanAnswer(answer.answer)}</span>
                            </p>
                            <p class="res">
                                <span class="bold">Sources: ${getDocuments(answer.meta.titles)}</span>
                            </p>`
                        }
                        let node = document.createElement("section");
                        node.classList.add('response')
                        node.innerHTML = ansSec
                        answersDiv.appendChild(node);
                    }
                }
                let debugInfo = getValue('debug-info');
                if (debugInfo == 'false') {
                    debugInfo = false;
                } else {
                    debugInfo = true;
                }
                if (!debugInfo) {
                    debugSection.innerText = JSON.stringify(response, null, 4)
                    debugInfoHeader.style.display = 'none'
                    debugInfoSection.style.display = 'none'
                    debugSection.style.display = 'none';
                } else {
                    debugSection.innerText = JSON.stringify(response, null, 4)
                    debugInfoHeader.style.display = 'block'
                    debugInfoSection.style.display = 'block'
                    debugSection.style.display = 'block';
                }
            } else {
                showNotification(response.msg, 'error')
            }
            setLoading(false)
        } else {
            showNotification('Enter a valid search term', 'error')
        }
    } catch (e) {
        console.log(e)
        setLoading(false)
        resultsSection.style.display = 'none';
        showNotification(e.message + '. Ensure the server is running', 'error')
    }
}

async function ExtractiveQuery() {
    try {
        if (query.value.trim().length > 1) {
            setLoading(true)
            const request = await fetch('http://127.0.0.1:5000/extractive-query', {
                method: "POST",
                body: JSON.stringify({
                    'query': query.value,
                    'max-doc': parseInt(getValue('max-doc')),
                    'max-ans': parseInt(getValue('max-ans'))
                })
            })
            const response = await request.json()
            if (response.error == false) {
                for (answer of response.answers) {
                    if (answer.answer.length > 1) {
                        let ansSec = '';
                        if (answer.type == 'extractive') {
                            ansSec = `
                            <p class="res">
                                <span>...${cleanExtractiveAnswer(answer.context, answer.answer)}...</span>
                            </p>
                            <p class="res">
                                <span class="bold">Relevance: </span> 
                                <span>${Math.round(answer.score * 100) / 100}</span>
                            </p>
                            <p class="res">
                                <span class="bold">Source: </span> 
                                <span>${answer.meta.name} - </span>
                                <span class="bold">Page Number: </span> 
                                <span>${answer.meta.page}</span>
                            </p>
                            `
                        } else {
                            ansSec = `
                            <p class="res">
                                <span>${cleanAnswer(answer.answer)}</span>
                            </p>
                            <p class="res">
                                <span class="bold">Sources: ${getDocuments(answer.meta.titles)}</span>
                            </p>`
                        }
                        let node = document.createElement("section");
                        node.classList.add('response')
                        node.innerHTML = ansSec
                        answersDiv.appendChild(node);
                    }
                }
                let debugInfo = getValue('debug-info');
                if (debugInfo == 'false') {
                    debugInfo = false;
                } else {
                    debugInfo = true;
                }
                if (!debugInfo) {
                    debugSection.innerText = JSON.stringify(response, null, 4)
                    debugInfoHeader.style.display = 'none'
                    debugInfoSection.style.display = 'none'
                    debugSection.style.display = 'none';
                } else {
                    debugSection.innerText = JSON.stringify(response, null, 4)
                    debugInfoHeader.style.display = 'block'
                    debugInfoSection.style.display = 'block'
                    debugSection.style.display = 'block';
                }
            } else {
                showNotification(response.msg, 'error')
            }
            setLoading(false)
        } else {
            showNotification('Enter a valid search term', 'error')
        }
    } catch (e) {
        console.log(e)
        setLoading(false)
        resultsSection.style.display = 'none';
        showNotification(e.message + '. Ensure the server is running', 'error')
    }
}

function setLoading(value) {
    loading = value
    if (loading) {
        answersDiv.innerHTML = '';
        loadingSection.style.display = 'flex';
        resultsSection.style.display = 'none';
    } else {
        loadingSection.style.display = 'none';
        resultsSection.style.display = 'block';
    }
}


function showNotification(message, type = 'info') {
    console.log(message)
    var snackbar = document.getElementById("snackbar");
    snackbar.innerText = message;

    if (type == 'error') {
        snackbar.style.backgroundColor = '#FF5556';
    } else {
        snackbar.style.backgroundColor = '#E89347';
    }

    snackbar.className = "show";

    setTimeout(function () {
        snackbar.className = snackbar.className.replace("show", "");
    }, 1990);
}

function cleanAnswer(value) {
    value = value.replaceAll('\n', ' ')
    return value.trim()
}

function cleanExtractiveAnswer(value, answer) {
    value = value.replaceAll('\n', ' ')
    ansDiv = `
        <span class='ans'>${answer}<span class='super-ans'>answer</span></span>
    `;
    value = value.replace(answer, ansDiv);
    return value.trim()
}


