package gorm

import (
	"time"

	"gorm.io/gorm/logger"
)

type Option func(*Client)

func SetLogger(writer logger.Writer) func(*Client) {
	newLogger := logger.New(
		writer,
		logger.Config{
			SlowThreshold:             time.Second,   // 慢 SQL 阈值
			LogLevel:                  logger.Silent, // 日志级别
			IgnoreRecordNotFoundError: true,          // 忽略ErrRecordNotFound（记录未找到）错误
			Colorful:                  false,         // 禁用彩色打印
		},
	)
	return func(c *Client) {
		c.Logger = &newLogger
	}
}
