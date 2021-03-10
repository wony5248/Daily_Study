'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class room extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
      models.room.belongsTo(models.user, {
        foreignKey: "user_id"
      })
      models.room.hasMany(models["room_image"], {
        foreignKey: "room_id"
      })
      models.room.hasMany(models["room_option"], {
        foreignKey: "room_id"
      })
    }
  };
  room.init({
    user_id: DataTypes.INTEGER,
    price: DataTypes.STRING,
    room_size: DataTypes.STRING,
    title: DataTypes.STRING,
    content: DataTypes.STRING,
    location: DataTypes.STRING,
    latitude: DataTypes.STRING,
    longitude: DataTypes.STRING
  }, {
    sequelize,
    modelName: 'room',
    paranoid: true
  });
  return room;
};