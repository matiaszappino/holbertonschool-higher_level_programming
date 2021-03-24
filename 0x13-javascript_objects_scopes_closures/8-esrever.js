#!/usr/bin/node
exports.esrever = function (list) {
  const newarray = [];
  const len = list.length - 1;
  for (let i = len; i >= 0; i--) {
    newarray.push(list[i]);
  }
  return (newarray);
};
