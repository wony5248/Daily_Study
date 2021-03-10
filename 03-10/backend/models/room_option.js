'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class room_option extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
      models["room_option"].belongsTo(models.room, {foreignKey:"room_id"})
      //models.room_option = models["room_option"]이랑 같은것 -> _있을때는 [] 선호
    }
  };
  room_option.init({
    room_id: DataTypes.INTEGER,
    item: DataTypes.STRING
  }, {
    sequelize,
    modelName: 'room_option',
  });
  return room_option;
};