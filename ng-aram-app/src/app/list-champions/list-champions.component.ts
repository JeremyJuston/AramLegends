import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-list-champions',
  templateUrl: './list-champions.component.html',
  styles: [
  ]
})
export class ListChampionsComponent {
  championsList: string[] = ['Ezreal', 'Lux', 'Garen'];
  champs: any;

  constructor(private http: HttpClient, private route: ActivatedRoute) {}

  ngOnInit() {
    const username: string|null = this.route.snapshot.paramMap.get('username')
    this.http.get(`loading/${username}`).subscribe((data: any) => {
      this.champs = data;
    })
    /**
    this.champs = [  ['John', 'Doe', 'john.doe@example.com', '35', 'Male', 'New York'],
    ['Jane', 'Smith', 'jane.smith@example.com', '27', 'Female', 'Los Angeles'],
    ['Bob', 'Johnson', 'bob.johnson@example.com', '42', 'Male', 'Chicago'],
    ['Alice', 'Williams', 'alice.williams@example.com', '21', 'Female', 'Houston']
  ];*/
  }

  

  sortBy = 0;
  reverse = true;

  sort(column: number) {
    if (this.sortBy === column) {
      this.reverse = !this.reverse;
    } else {
      this.sortBy = column;
      this.reverse = true;
    }
  }



}
