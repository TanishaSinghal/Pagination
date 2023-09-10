CREATE DATABASE rootUser;
use rootUser;
SELECT `aggapp_student`.`id`,
    `aggapp_student`.`name`,
    `aggapp_student`.`email`,
    `aggapp_student`.`document`,
    `aggapp_student`.`phone`,
    `aggapp_student`.`registrationDate`
FROM `rootuser`.`aggapp_student`;
