package config

import (
	"path/filepath"
	"runtime"

	"github.com/spf13/viper"
)

type (
	Config struct {
		MysqlSetting  Mysql  `mapstructure:"mysql"`
		LoggerSetting Logger `mapstructure:"logger"`
		HTTPSetting   HTTP   `mapstructure:"http"`
	}
	Mysql struct {
		Dsn string `mapstructure:"dsn"`
	}
	Logger struct {
		Level string `mapstructure:"level"`
	}
	HTTP struct {
		Port string `mapstructure:"port"`
	}
)

// BaseDir -.
// 获取绝对路径
func BaseDir() string {
	_, filename, _, _ := runtime.Caller(0)
	return filepath.Dir(filename)
}

// NewConfig -.
func NewConfig() (*Config, error) {
	viper.SetConfigName("config")
	viper.SetConfigType("yaml")
	viper.AddConfigPath(".")
	viper.AddConfigPath(BaseDir())
	if err := viper.ReadInConfig(); err != nil {
		return nil, err
	}
	config := &Config{}
	if err := viper.Unmarshal(config); err != nil {
		return nil, err
	}
	return config, nil
}
