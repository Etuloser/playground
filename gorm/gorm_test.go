package gorm

import (
	"fmt"
	"playground/config"
	"testing"
	"time"
)

type Users struct {
	ID           uint64    `gorm:"column:id;type:bigint(20) unsigned;"`
	Name         string    `gorm:"column:name;type:varchar(256);default:null"`
	Email        string    `gorm:"column:email;type:varchar(256);default:null"`
	Age          uint8     `gorm:"column:age;type:tinyint(3) unsigned;default:null"`
	Birthday     time.Time `gorm:"column:birthday;type:datetime;default:null"`
	MemberNumber string    `gorm:"column:member_number;type:varchar(256);default:null"`
	ActivatedAt  time.Time `gorm:"column:activated_at;type:datetime;default:null"`
	CreatedAt    time.Time `gorm:"column:created_at;type:datetime;default:null"`
	UpdatedAt    time.Time `gorm:"column:updated_at;type:datetime;default:null"`
}

type UserRepo struct {
	*Curd[Users]
}

func NewRepo(c *Client) *UserRepo {
	return &UserRepo{&Curd[Users]{c}}
}

func TestGorm(t *testing.T) {
	cfg, _ := config.NewConfig()
	client, _ := New(cfg.MysqlSetting.Dsn)
	userRepo := NewRepo(client)
	fmt.Println(userRepo)
}
