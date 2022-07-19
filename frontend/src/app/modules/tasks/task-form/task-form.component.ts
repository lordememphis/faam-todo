import { Component, Inject, OnInit } from "@angular/core";
import { FormBuilder, FormGroup } from "@angular/forms";
import { MAT_DIALOG_DATA } from "@angular/material/dialog";
import { TaskEntity, TaskFormDialogData } from "../../../data-access/models/task.model";

@Component({
  selector: "app-task-form",
  templateUrl: "./task-form.component.html",
  styleUrls: ["./task-form.component.css"],
})
export class TaskFormComponent implements OnInit {
  form!: FormGroup;

  constructor(private fb: FormBuilder, @Inject(MAT_DIALOG_DATA) readonly data: TaskFormDialogData) {}

  get task(): TaskEntity {
    return { ...this.form.value, _id: this.data.task?._id };
  }

  ngOnInit() {
    this.form = this.fb.group({
      title: this.data.task?.title,
      description: this.data.task?.description,
      completed: !!this.data.task?.completed,
    });
  }

  dialogClose() {}
}
