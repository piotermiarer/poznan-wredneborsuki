const teamShow = require('./team-show');
const offers = require('./offers');
const allTeams = require('./all-teams');

const initializeSearchbar = require('./searchbar');

document.addEventListener('DOMContentLoaded', () => {
    const route = document.querySelector('.main').getAttribute('id');
    initializeSearchbar(document.querySelector('#searchbar'));
    switch (route) {
        case 'team-show': teamShow(); break;
        case 'offers': offers(); break;
        case 'all-teams': allTeams(); break;
    }
});
