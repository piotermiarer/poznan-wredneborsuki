const SVGInjector = require('svg-injector');
const createFigure = require('./interactive-figure');
const utils = require('./utils');

module.exports = function teamShow() {
    injectSVGs({}).then(() => {
        const [teamName] = window.location.href.split('/').slice(-1);
        createFigure(document.querySelector('#player'), 'player', {
            shorts: () => goTo(`offers/${teamName}/shorts`),
            socks: () => goTo(`offers/${teamName}/socks`),
            shirt: () => goTo(`offers/${teamName}/shirt`),
            boots: () => goTo(`offers/${teamName}/boots`),
            ball: () => goTo(`offers/${teamName}/ball`)
        });
        createFigure(document.querySelector('#fan'), 'fan', {
            scarf: () => goTo(`offers/${teamName}/scarf`),
            hat: () => goTo(`offers/${teamName}/hat`),
            tracksuit: () => goTo(`offers/${teamName}/tracksuit`),
            shirt: () => goTo(`offers/${teamName}/hoodie`),
            boots: () => goTo(`offers/${teamName}/boots`)
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
