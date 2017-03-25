const utils = require('./utils');

module.exports = function searchbar(element) {
    const url = `${window.location.protocol}//${window.location.host}/search_team`;
    const input = element.querySelector('.searchbar__input');
    input.value = '';
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
            if (phrase.length < 3) displaySuggestions([], sugestions)
        }
        input.value = phrase;
    });
}

function getResultsForPhrase(url, phrase) {
    return fetch(`${url}/${phrase}`).then(res => res.json());
}

function displaySuggestions(results, container) {
    const children = utils.toArray(container.children);
    console.log(results);
    if (results > children) {
        children.forEach((child, i) => updateSuggestion(child, results[i]));
        results.slice(children.length).forEach((result, i) => createSuggestion(container, result));
    } else {
        results.forEach((result, i) => updateSuggestion(children[i], result));
        children.slice(results.length).forEach((child) => removeSuggestion(child));
    }
}

function updateSuggestion(sugestion, values) {
    const link = sugestion.querySelector('a');
    const image = sugestion.querySelector('img');
    const p = sugestion.querySelector('p');
    p.innerText = values[0][0];
    link.setAttribute('href', `/team_show/${values[0][0]}`)
}
function createSuggestion(container, values) {
    const el = document.createElement('li');
    const link = document.createElement('a');
    const image = document.createElement('img');
    const p = document.createElement('p');
    el.classList.add('sugestion');
    link.classList.add('sugestion__link');
    link.setAttribute('href', `/team_show/${values[0][0]}`)
    // image.classList.add('sugestion__image');
    // image.setAttribute('src', `/static/images/${name}`)
    p.classList.add('sugestion__name');
    p.innerText = values[0][0];
    link.appendChild(p);
    el.appendChild(link);
    container.appendChild(el);
}
function removeSuggestion(el) {
    el.parentNode.removeChild(el);
}
