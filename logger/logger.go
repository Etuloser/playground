package logger

import (
	"fmt"
	"os"

	"github.com/sirupsen/logrus"
)

// Interface -.
type Interface interface {
	Debug(args ...interface{})
	Info(args ...interface{})
	Warn(args ...interface{})
	Error(args ...interface{})
	Fatal(args ...interface{})
}

// Logger -.
type Logger struct {
	logger *logrus.Logger
}

// 指针实现一下接口
var _ Interface = (*Logger)(nil)

// New -.
func New(level string) *Logger {
	logger := logrus.New()
	// Log as JSON instead of the default ASCII formatter.
	logger.SetFormatter(&logrus.JSONFormatter{})

	// Output to stdout instead of the default stderr
	// Can be any io.Writer, see below for File example
	logger.SetOutput(os.Stdout)

	// Only log the warning severity or above.
	l, err := logrus.ParseLevel(level)
	if err != nil {
		panic(err)
	}
	logger.SetLevel(l)
	return &Logger{logger: logger}
}

// 实现gorm.logger.Writer
func (l *Logger) Printf(format string, v ...interface{}) {
	logStr := fmt.Sprintf(format, v...)
	l.logger.Info(logStr)
}

// Debug -.
func (l *Logger) Debug(args ...interface{}) {
	l.logger.Debug(args)
}

// Info -.
func (l *Logger) Info(args ...interface{}) {
	l.logger.Info(args)
}

// Warn -.
func (l *Logger) Warn(args ...interface{}) {
	l.logger.Warn(args)
}

// Error -.
func (l *Logger) Error(args ...interface{}) {
	l.logger.Error(args)
}

// Fatal  -.
func (l *Logger) Fatal(args ...interface{}) {
	l.logger.Fatal(args)
}
