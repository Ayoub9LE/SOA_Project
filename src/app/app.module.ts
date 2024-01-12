import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MissionComponent } from './mission/mission.component';
import { RembouresementComponent } from './rembouresement/rembouresement.component';
import { AddmissionComponent } from './addmission/addmission.component';
import { AddremComponent } from './addrem/addrem.component';

@NgModule({
  declarations: [
    AppComponent,
    MissionComponent,
    RembouresementComponent,
    AddmissionComponent,
    AddremComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
