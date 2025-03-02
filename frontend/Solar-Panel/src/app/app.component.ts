import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from './header/header.component';
import {WelcomeComponent} from './welcome/welcome.component';
import { ServicesComponent } from './services/services.component';


@Component({
  selector: 'app-root',
  imports: [
    RouterOutlet, 
    HeaderComponent,
    WelcomeComponent,
    ServicesComponentcd 

  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {

  counter: number = 0
  title = 'solar-panel';

  add(){
    this.counter++;
  }
}
