
module.exports = {
    toArray(list) {
        return Array.prototype.slice.call(list, 0);
    },
    reduceNumber(number, pcnt) {
        const result = number * (1 - pcnt);
        return result > 255 ? 255 : parseInt(result);
    },
    objectForEach(obj, fn) {
        for (let key in obj) {
            if (obj.hasOwnProperty(key)) {
                fn.call(obj, key, obj[key], obj);
            }
        }
    },
    objectMap(obj, fn) {
        const result  = {};
        for (let key in obj) {
            if (obj.hasOwnProperty(key)) {
                result[key] = fn.call(obj, key, obj[key], obj);
            }
        }
        return result;
    },
    debounce(fn, delay) {
        let timeoutID;

        return function(...args) {
            if (timeoutID) clearTimeout(timeoutID);
            timeoutID = setTimeout(() => {
                fn.apply(null, args);
            }, delay);
        }

    }

}
