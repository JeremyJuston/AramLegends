import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { ListChampionsComponent } from './list-champions/list-champions.component';

const routes: Routes = [
  {path: 'champions/:username', component: ListChampionsComponent},
  {path: 'home', component: HomeComponent},
  {path: '', redirectTo:'home', pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
