#!/usr/bin/node
exports.esrever = function (list) {
    const new_array = [];
    const len = list.length - 1;
    for (let i = len; i >= 0; i--) {
      new_array.push(list[i]);
    }
    return (new_array);
  };