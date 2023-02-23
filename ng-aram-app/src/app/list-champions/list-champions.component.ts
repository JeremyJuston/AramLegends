import { Component } from '@angular/core';

@Component({
  selector: 'app-list-champions',
  templateUrl: './list-champions.component.html',
  styles: [
  ]
})
export class ListChampionsComponent {
  championsList: string[] = ['Ezreal', 'Lux', 'Garen'];
}
