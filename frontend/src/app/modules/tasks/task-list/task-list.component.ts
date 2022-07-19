import { Component, OnInit } from "@angular/core";
import { MatDialog } from "@angular/material/dialog";
import { filter, switchMap } from "rxjs";
import { DataService } from "../../../data-access/data.service";
import { TaskEntity } from "../../../data-access/models/task.model";
import { TaskFormComponent } from "../task-form/task-form.component";

@Component({
  selector: "app-task-list",
  templateUrl: "./task-list.component.html",
  styleUrls: ["./task-list.component.scss"],
})
export class TaskListComponent implements OnInit {
  tasks$ = this.data.getAllTasks();

  constructor(private data: DataService, private dialog: MatDialog) {}

  ngOnInit(): void {}

  createTask() {
    this.tasks$ = this.dialog
      .open(TaskFormComponent, { data: { action: "ADD TASK", title: "Add new task" } })
      .afterClosed()
      .pipe(
        filter((data) => !!data),
        switchMap((data) => this.data.createTask(data.task)),
        switchMap(() => this.data.getAllTasks())
      );
  }

  updateTask(task: TaskEntity) {
    this.tasks$ = this.dialog
      .open(TaskFormComponent, { data: { action: "UPDATE TASK", title: "Edit task", task } })
      .afterClosed()
      .pipe(
        filter((data) => !!data),
        switchMap((data: { task: TaskEntity; action: string }) => {
          if (data.action === "DELETE") return this.data.deleteTask(data.task._id);
          return this.data.updateTask(data.task);
        }),
        switchMap(() => this.data.getAllTasks())
      );
  }
}
