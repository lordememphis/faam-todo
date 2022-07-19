export interface TaskEntity {
  _id: string;
  title: string;
  description: string;
  completed: boolean;
}

export interface PartialTaskEntity extends Partial<TaskEntity> {}

export interface TaskFormDialogData {
  title: string;
  action: string;
  task?: TaskEntity;
}
