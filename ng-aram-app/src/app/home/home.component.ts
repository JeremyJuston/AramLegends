import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styles: [
  ]
})
export class HomeComponent implements OnInit {
  ngOnInit() {
  }

  testInput(inputText: string) {
    console.log(`Vous avez entré ${inputText}`)
    history.pushState({}, '', `/champions/${inputText}`)
    location.reload();
    //this.refreshPage();
}

refreshPage() {
    // Recharger la page pour obtenir les nouveaux résultats de recherche
    location.reload();
}

/**window.addEventListener('popstate', () => {
    this.refreshPage();
});
*/
}
