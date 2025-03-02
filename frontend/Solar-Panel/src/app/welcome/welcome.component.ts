import { Component } from '@angular/core';

@Component({
  selector: 'app-welcome',
  imports: [],
  templateUrl: './welcome.component.html',
  styleUrl: './welcome.component.css'
})
export class WelcomeComponent {


  welcomeStatement: string = "Welcome to ShellShock ⚡"
  shellShockDescription : string = "A Solar Powered Montering App"

}
