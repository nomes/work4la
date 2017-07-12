CREATE TABLE exam_subscription (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `time_created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `time_sent` TIMESTAMP NULL DEFAULT NULL,
  `email_address` VARCHAR(254) NOT NULL,
  `job_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX job_id_idx (`job_id`)
) ENGINE=InnoDB;
