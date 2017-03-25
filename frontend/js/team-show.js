const SVGInjector = require('svg-injector');
const createFigure = require('./interactive-figure');
const utils = require('./utils');

module.exports = function teamShow() {
    injectSVGs({}).then(() => {
        const [teamName] = window.location.href.split('/').slice(-1);
        createFigure(document.querySelector('#player'), 'player', {
            shorts: () => goTo(`offers/${teamName}/spodenki`),
            socks: () => goTo(`offers/${teamName}/getry`),
            shirt: () => goTo(`offers/${teamName}/koszulka`),
            boots: () => goTo(`offers/${teamName}/buty`),
            ball: () => goTo(`offers/${teamName}/piłka`)
        });
        createFigure(document.querySelector('#fan'), 'fan', {
            scarf: () => goTo(`offers/${teamName}/szalik`),
            hat: () => goTo(`offers/${teamName}/czapka`),
            tracksuit: () => goTo(`offers/${teamName}/dres`),
            shirt: () => goTo(`offers/${teamName}/koszulka`),
            boots: () => goTo(`offers/${teamName}/buty`)
        });
    });
}

function goTo(url) {
    window.location.href = `${window.location.protocol}//${window.location.host}/${url}`;
}

function injectSVGs(opts) {
    const toInject = utils.toArray(document.querySelectorAll('img.svg-injection'));
    return new Promise((resolve, reject) => {
        SVGInjector(toInject, opts, count => {
            if (count != toInject.length) reject('Some elements hasn\'t been inserted');
            else resolve();
        });
    });
}

const playerElements = {};
