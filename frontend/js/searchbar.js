const utils = require('./utils');

module.exports = function searchbar(element) {
    const url = `${window.location.protocol}//${window.location.host}/search_team`;
    const input = element.querySelector('.searchbar__input');
    const sugestions = element.querySelector('.searchbar__sugestions-list');
    let phrase = '';

    const fn = utils.debounce(phrase => {
        getResultsForPhrase(url, phrase).then(response => displaySuggestions(response, sugestions));
    }, 500);

    input.addEventListener('keypress', event => {
        phrase += event.key;
        input.value = phrase;
        if (phrase.length > 3) fn(phrase);
        event.preventDefault();
    });
    input.addEventListener('keydown', event => {
        if (event.key === 'Backspace') {
            if (phrase.length) phrase = phrase.slice(0, -1);
        }
        input.value = phrase;
    });
}

function getResultsForPhrase(url, phrase) {
    return fetch(`${url}/${phrase}`).then(res => res.json());
}

function displaySuggestions(results, container) {
    const children = utils.toArray(container.children);
    if (results > children) {
        children.forEach((child, i) => updateSuggestion(child, results[i][i]));
        results.slice(children.length).forEach((result, i) => createSuggestion(container, result[i]));
    } else {
        results.forEach((result, i) => updateSuggestion(children[i], result[i]));
        children.slice(results.length).forEach((child) => removeSuggestion(child));
    }
}

function updateSuggestion(sugestion, name) {
    const link = sugestion.querySelector('a');
    const image = sugestion.querySelector('img');
    const p = sugestion.querySelector('p');
    p.innerText = name;
    link.setAttribute('href', `/team_show/${name}`)
}
function createSuggestion(container, name) {
    const el = document.createElement('li');
    const link = document.createElement('a');
    const image = document.createElement('img');
    const p = document.createElement('p');
    el.classList.add('sugestion');
    link.classList.add('sugestion__link');
    link.setAttribute('href', `/team_show/${name}`)
    // image.classList.add('sugestion__image');
    // image.setAttribute('src', `/static/images/${name}`)
    p.classList.add('sugestion__name');
    p.innerText = name;
    link.appendChild(p);
    el.appendChild(link);
    container.appendChild(el);
}
function removeSuggestion(el) {
    el.parentNode.removeChild(el);
}
