import { Component, Input } from "@angular/core";
import { TaskEntity } from "../../../data-access/models/task.model";

@Component({
  selector: "app-task",
  templateUrl: "./task.component.html",
  styleUrls: ["./task.component.css"],
})
export class TaskComponent {
  @Input() task!: TaskEntity;
}
