const utils = require('./utils');

const segmentNamesForType = {
    player: {
        'shorts': [ 'shorts-p1', 'shorts-p2', 'shorts-inside-p1', 'shorts-inside-p2' ],
        'socks': [ 'socks' ],
        'shirt': [ 'shirt-top', 'shirt-back' ],
        'boots': [ 'boot1-top', 'boot2-top', 'boot1-down', 'boot2-down'],
        'ball': [ 'ball' ]
    },
    fan: {
        'scarf': [ 'scarf' ],
        'hat': [ 'hat' ],
        'tracksuit': [ 'tracksuit-down' ],
        'shirt': [ 'shirt-fan' ],
        'boots': [ 'boot1-top-fan', 'boot2-top-fan', 'boot1-down-fan', 'boot2-down-fan']
    }
};

module.exports = function createIntractiveFigure(svg, type, handlers) {
    const self = {};
    const segmentsNames = segmentNamesForType[type];
    if (!segmentsNames) throw 'Unexpected figure type';

    const segmentsElements = utils.objectMap(segmentsNames, (key, segments) => {
        return segments.map(seg => svg.querySelector(`#${seg}`));
    });
    utils.objectForEach(segmentsElements, (key, segments) => {
        segments.forEach(seg => {
            seg.gearGroup = key;
            seg.initialFill = seg.style.fill;
            registerHandlers(seg, handlers[key], segmentsElements);
            darkenElement(seg, 0.5);
        });
    });

    self.elements = segmentsElements;
    return self;
}

function registerHandlers(segment, clickHandler, allSegments) {
    segment.addEventListener('mouseenter', event => {
        allSegments[event.target.gearGroup].forEach(el => resetElement(el));
    });
    segment.addEventListener('mouseleave', event => {
        allSegments[event.target.gearGroup].forEach(el => darkenElement(el, 0.5));
    });
    segment.addEventListener('click', event => {
        clickHandler.call(null, null);
    });

}

function darkenElement(el, pcnt) {
    if (el.tagName === 'g') {
        utils.toArray(el.children).forEach(child => darken(child, pcnt));
    } else {
        darken(el, pcnt);
    }
}

function resetElement(el) {
    if (el.tagName === 'g') {
        utils.toArray(el.children).forEach(child => reset(child));
    } else {
        reset(el);
    }
}

function reset(el) {
    el.style.fill = el.initialFill;
}

function darken(el, pcnt) {
    const val = el.style.fill.slice(4, -1).split(',').map(s => parseFloat(s)).map(n => utils.reduceNumber(n, pcnt));
    el.initialFill = el.style.fill;
    el.style.fill = `rgb(${val[0]}, ${val[1]}, ${val[2]})`;
}
