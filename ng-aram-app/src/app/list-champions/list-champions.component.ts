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
  username: string|null = "Test";

  constructor(private http: HttpClient, private route: ActivatedRoute) {}

  ngOnInit() {
    
    this.username = this.route.snapshot.paramMap.get('username')
    this.http.get(`loading/${this.username}`).subscribe((data: any) => {
      this.champs = data;
    })
    /**
    this.champs = [  ['John', 'Doe', 'john.doe@example.com', '35', 'Male', 'New York', '25'],
    ['Jane', 'Smith', 'jane.smith@example.com', '27', 'Female', 'Los Angeles', '2'],
    ['Bob', 'Johnson', 'bob.johnson@example.com', '42', 'Male', 'Chicago', '5'],
    ['Alice', 'Williams', 'alice.williams@example.com', '21', 'Female', 'Houston', '40']
  ];*/
    console.log(this.champs);
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
