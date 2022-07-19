import { CommonModule } from "@angular/common";
import { NgModule } from "@angular/core";
import { ReactiveFormsModule } from "@angular/forms";
import { MaterialModule } from "../../core/material.module";
import { TaskFormComponent } from "./task-form/task-form.component";
import { TaskListComponent } from "./task-list/task-list.component";
import { TaskComponent } from "./task/task.component";

@NgModule({
  declarations: [TaskFormComponent, TaskComponent, TaskListComponent],
  imports: [CommonModule, MaterialModule, ReactiveFormsModule],
  exports: [TaskListComponent],
})
export class TasksModule {}
