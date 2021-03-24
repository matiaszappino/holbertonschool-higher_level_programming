#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
    let number_occurrences = 0;
    list.forEach(aux => {
        if (aux === searchElement) {
            number_occurrences += 1;
        }
    });
    return number_occurrences;
};