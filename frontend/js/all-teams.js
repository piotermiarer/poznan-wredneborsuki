const utils = require('./utils');

module.exports = function allTeams() {
    const containers = document.getElementsByClassName('league-container');
    const links = document.getElementsByClassName('league-link');
    const leagueLinkMap = {};

    utils.toArray(links).forEach((link, i) => {
        leagueLinkMap[link.getAttribute('data-league')] = { link };
        if (i == 0) link.setAttribute('data-active', true);
    });
    utils.toArray(containers).forEach(container => {
        leagueLinkMap[container.getAttribute('data-league')].container = container;
    });

    hideInactive(leagueLinkMap);

    utils.objectForEach(leagueLinkMap, (_, {link, container}) => {
        link.addEventListener('click', event => {
            swapActive(leagueLinkMap);
            event.target.setAttribute('data-active', true);
            hideInactive(leagueLinkMap);
        });
    });
}

function swapActive(leagues) {
    utils.objectForEach(leagues, (_, {link, container}) => {
        if (link.getAttribute('data-active')) link.removeAttribute('data-active');
    });
}
function hideInactive(leagues) {
    utils.objectForEach(leagues, (_, {link, container}) => {
        if (link.getAttribute('data-active')) container.style.display = 'block';
        else container.style.display = 'none';
    });
}
