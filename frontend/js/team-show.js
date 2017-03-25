const SVGInjector = require('svg-injector');
const createFigure = require('./interative-figure');
const utils = require('./utils');

module.exports = function teamShow() {
    injectSVGs({}).then(() => {
        createFigure(document.querySelector('#player'), 'player', {
            shorts() { console.log('shorts'); },
            socks() { console.log('socks'); },
            shirt() { console.log('shirt'); },
            boots() { console.log('boots'); },
            ball() { console.log('ball'); }
        });
        createFigure(document.querySelector('#fan'), 'fan', {
            scarf() { console.log('scarf'); },
            hat() { console.log('hat'); },
            tracksuit() { console.log('tracksuit'); },
            shirt() { console.log('shirt'); },
            boots() { console.log('boots'); }
        });
    });
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
