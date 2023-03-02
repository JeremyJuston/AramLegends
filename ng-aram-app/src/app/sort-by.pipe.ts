import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'sortBy'
})
export class SortByPipe implements PipeTransform {
  transform(array: any[][], field: number, reverse: boolean = false): any[][] {
    if (!array || array.length === 0 || !field || field >= array[0].length) {
      return array;
    }

    array.sort((a: any[], b: any[]) => {
      let aValue = a[field];
      let bValue = b[field];

      if (typeof aValue === 'string') {
        aValue = aValue.toLowerCase();
      }

      if (typeof bValue === 'string') {
        bValue = bValue.toLowerCase();
      }

      if (aValue < bValue) {
        return reverse ? 1 : -1;
      } else if (aValue > bValue) {
        return reverse ? -1 : 1;
      } else {
        return 0;
      }
    });

    return array;
  }
}
