
const teamShow = require('./team-show');
const offers = require('./offers');

document.addEventListener('DOMContentLoaded', () => {
    const route = document.querySelector('.main').getAttribute('id');
    switch (route) {
        case 'team-show': teamShow(); break;
        case 'offers': offers(); break;
    }
});
