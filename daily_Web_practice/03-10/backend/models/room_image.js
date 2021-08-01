'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class room_image extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
      models["room_image"].belongsTo(models.room, {foreignKey:"room_id"})
    }
  };
  room_image.init({
    room_id: DataTypes.INTEGER,
    file_name: DataTypes.STRING,
    original_file_name: DataTypes.STRING
  }, {
    sequelize,
    modelName: 'room_image',
  });
  return room_image;
};