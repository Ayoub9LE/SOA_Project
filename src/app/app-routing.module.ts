import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MissionComponent } from './mission/mission.component';
import { RembouresementComponent } from './rembouresement/rembouresement.component';
import { AddmissionComponent } from './addmission/addmission.component';
import { AddremComponent } from './addrem/addrem.component';






const routes: Routes = [
  { path: 'mission', component: MissionComponent },
  { path: 'rem', component: RembouresementComponent },
  { path: 'addmission', component: AddmissionComponent },
  { path: 'addrem', component: AddremComponent },
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
