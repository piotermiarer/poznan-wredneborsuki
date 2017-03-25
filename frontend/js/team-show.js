const SVGInjector = require('svg-injector');
const createFigure = require('./interactive-figure');
const utils = require('./utils');

module.exports = function teamShow() {
    injectSVGs({}).then(() => {
        const [teamName] = window.location.href.split('/').slice(-1);
        createFigure(document.querySelector('#player'), 'player', {
            shorts: () => goTo(`offers/${teamName}/spodenki/1`),
            socks: () => goTo(`offers/${teamName}/getry/1`),
            shirt: () => goTo(`offers/${teamName}/koszulka/1`),
            boots: () => goTo(`offers/${teamName}/buty/1`),
            ball: () => goTo(`offers/${teamName}/piłka/1`)
        });
        createFigure(document.querySelector('#fan'), 'fan', {
            scarf: () => goTo(`offers/${teamName}/szalik/1`),
            hat: () => goTo(`offers/${teamName}/czapka/1`),
            tracksuit: () => goTo(`offers/${teamName}/dres/1`),
            shirt: () => goTo(`offers/${teamName}/koszulka/1`),
            boots: () => goTo(`offers/${teamName}/buty/1`)
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
