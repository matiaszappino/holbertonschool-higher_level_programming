#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let numberoccurrences = 0;
  list.forEach(aux => {
    if (aux === searchElement) {
      numberoccurrences += 1;
    }
  });
  return numberoccurrences;
};
