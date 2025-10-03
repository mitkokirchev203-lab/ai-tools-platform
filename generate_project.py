import zipfile

# --------------------------------------------------
# AI Tools Platform - Full Project Generator (с миграции и seeders)
# --------------------------------------------------

project_files = {
    # ---------- Root ----------
    "ai-tools-platform/README.md": """# 🚀 AI Tools Sharing Platform
Full-stack приложение (Laravel + Next.js + Docker) за вътрешно споделяне на AI инструменти.
""",
    "ai-tools-platform/.gitignore": """.env
/vendor
/node_modules
.next
/storage
*.log
.DS_Store
Thumbs.db
""",
    "ai-tools-platform/docker-compose.yml": """version: "3.8"
services:
  laravel:
    build: ./backend
    container_name: laravel_app
    ports:
      - "8201:80"
    volumes:
      - ./backend:/var/www/html
    depends_on:
      - mysql
      - redis

  mysql:
    image: mysql:8.0
    container_name: mysql_db
    environment:
      MYSQL_DATABASE: aitools
      MYSQL_USER: aitools
      MYSQL_PASSWORD: secret
      MYSQL_ROOT_PASSWORD: root
    ports:
      - "3307:3306"

  redis:
    image: redis:alpine
    container_name: redis_cache
    ports:
      - "6379:6379"

  nextjs:
    build: ./frontend
    container_name: nextjs_app
    ports:
      - "8200:3000"
    volumes:
      - ./frontend:/app
    command: npm run dev
""",

    # ---------- Backend Dockerfile ----------
    "ai-tools-platform/backend/Dockerfile": """FROM laravelphp/php-fpm:8.2
WORKDIR /var/www/html
COPY . .
RUN composer install
CMD php artisan serve --host=0.0.0.0 --port=80
""",

    # ---------- Laravel миграции ----------
    "ai-tools-platform/backend/database/migrations/2025_01_01_000001_create_roles_table.php": """<?php
use Illuminate\\Database\\Migrations\\Migration;
use Illuminate\\Database\\Schema\\Blueprint;
use Illuminate\\Support\\Facades\\Schema;

return new class extends Migration {
    public function up(): void {
        Schema::create('roles', function (Blueprint $table) {
            $table->id();
            $table->string('name')->unique();
            $table->timestamps();
        });
    }
    public function down(): void { Schema::dropIfExists('roles'); }
};
""",
    "ai-tools-platform/backend/database/migrations/2025_01_01_000002_create_users_table.php": """<?php
use Illuminate\\Database\\Migrations\\Migration;
use Illuminate\\Database\\Schema\\Blueprint;
use Illuminate\\Support\\Facades\\Schema;

return new class extends Migration {
    public function up(): void {
        Schema::create('users', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->string('email')->unique();
            $table->string('password');
            $table->foreignId('role_id')->constrained();
            $table->timestamps();
        });
    }
    public function down(): void { Schema::dropIfExists('users'); }
};
""",
    "ai-tools-platform/backend/database/migrations/2025_01_01_000003_create_categories_table.php": """<?php
use Illuminate\\Database\\Migrations\\Migration;
use Illuminate\\Database\\Schema\\Blueprint;
use Illuminate\\Support\\Facades\\Schema;

return new class extends Migration {
    public function up(): void {
        Schema::create('categories', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->string('slug')->unique();
            $table->timestamps();
        });
    }
    public function down(): void { Schema::dropIfExists('categories'); }
};
""",
    "ai-tools-platform/backend/database/migrations/2025_01_01_000004_create_tools_table.php": """<?php
use Illuminate\\Database\\Migrations\\Migration;
use Illuminate\\Database\\Schema\\Blueprint;
use Illuminate\\Support\\Facades\\Schema;

return new class extends Migration {
    public function up(): void {
        Schema::create('tools', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->text('description')->nullable();
            $table->string('link');
            $table->foreignId('category_id')->constrained();
            $table->foreignId('created_by')->constrained('users');
            $table->enum('status',['pending','approved','rejected'])->default('pending');
            $table->timestamps();
        });
    }
    public function down(): void { Schema::dropIfExists('tools'); }
};
""",

    # ---------- Seeders ----------
    "ai-tools-platform/backend/database/seeders/RoleSeeder.php": """<?php
namespace Database\\Seeders;
use Illuminate\\Database\\Seeder;
use Illuminate\\Support\\Facades\\DB;

class RoleSeeder extends Seeder {
    public function run(): void {
        DB::table('roles')->insert([
            ['name'=>'owner'],
            ['name'=>'backend'],
            ['name'=>'frontend'],
            ['name'=>'pm'],
            ['name'=>'qa'],
            ['name'=>'designer']
        ]);
    }
}
""",
    "ai-tools-platform/backend/database/seeders/UserSeeder.php": """<?php
namespace Database\\Seeders;
use Illuminate\\Database\\Seeder;
use Illuminate\\Support\\Facades\\DB;
use Illuminate\\Support\\Facades\\Hash;

class UserSeeder extends Seeder {
    public function run(): void {
        DB::table('users')->insert([
            ['name'=>'Иван Иванов','email'=>'ivan@admin.local','password'=>Hash::make('password'),'role_id'=>1],
            ['name'=>'Елена Петрова','email'=>'elena@frontend.local','password'=>Hash::make('password'),'role_id'=>3],
            ['name'=>'Петър Георгиев','email'=>'petar@backend.local','password'=>Hash::make('password'),'role_id'=>2],
        ]);
    }
}
""",
    "ai-tools-platform/backend/database/seeders/CategorySeeder.php": """<?php
namespace Database\\Seeders;
use Illuminate\\Database\\Seeder;
use Illuminate\\Support\\Facades\\DB;

class CategorySeeder extends Seeder {
    public function run(): void {
        DB::table('categories')->insert([
            ['name'=>'Chatbots','slug'=>'chatbot'],
            ['name'=>'NLP','slug'=>'nlp'],
            ['name'=>'Computer Vision','slug'=>'vision']
        ]);
    }
}
""",
    "ai-tools-platform/backend/database/seeders/ToolSeeder.php": """<?php
namespace Database\\Seeders;
use Illuminate\\Database\\Seeder;
use Illuminate\\Support\\Facades\\DB;

class ToolSeeder extends Seeder {
    public function run(): void {
        DB::table('tools')->insert([
            ['name'=>'ChatGPT','description'=>'AI Chatbot','link'=>'https://chat.openai.com','category_id'=>1,'created_by'=>1,'status'=>'approved']
        ]);
    }
}
""",
    "ai-tools-platform/backend/database/seeders/DatabaseSeeder.php": """<?php
namespace Database\\Seeders;
use Illuminate\\Database\\Seeder;

class DatabaseSeeder extends Seeder {
    public function run(): void {
        $this->call([
            RoleSeeder::class,
            UserSeeder::class,
            CategorySeeder::class,
            ToolSeeder::class,
        ]);
    }
}
"""
}

# --------------------------------------------------
# Generate ZIP
# --------------------------------------------------
with zipfile.ZipFile("ai-tools-platform.zip", "w") as zipf:
    for path, content in project_files.items():
        zipf.writestr(path, content)

print("✅ Готово! Създаден е файл: ai-tools-platform.zip (с миграции и seeders)")

