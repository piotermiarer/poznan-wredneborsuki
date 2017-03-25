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
    return fetch(`${url}/${phrase}`);
}

function displaySuggestions(results, container) {
    
}
