import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http'

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ListChampionsComponent } from './list-champions/list-champions.component';
import { HomeComponent } from './home/home.component';
import { SortByPipe } from './sort-by.pipe';


@NgModule({
  declarations: [
    AppComponent,
    ListChampionsComponent,
    HomeComponent,
    SortByPipe
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
