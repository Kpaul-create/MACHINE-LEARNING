import { Server } from "socket.io";
import Redis from 'ioredis'

const redisHost = process.env.REDIS_HOST;
const redisPort = process.env.REDIS_PORT ? Number(process.env.REDIS_PORT) : undefined;
const redisUsername = process.env.REDIS_USERNAME;
const redisPassword = process.env.REDIS_PASSWORD;

const pub = new Redis({
  host: redisHost,
  port: redisPort,
  username: redisUsername,
  password: redisPassword,
});
const sub = new Redis({
  host: redisHost,
  port: redisPort,
  username: redisUsername,
  password: redisPassword,
});

class SocketService {
  private _io: Server;

  constructor() {
    console.log("Init Socket Service...");
    if (!redisHost || !redisPort || !redisPassword) {
      console.warn("Redis connection env vars missing. Set REDIS_HOST, REDIS_PORT, REDIS_PASSWORD.");
    }
    this._io = new Server({
      cors: {
        allowedHeaders: ["*"],
        origin: "*",
      },
    });
    sub.subscribe('MESSAGES');
  }

  public initListeners() {
    const io = this.io;
    console.log("Init Socket Listeners...");

    io.on("connect", (socket) => {
      console.log(`New Socket Connected`, socket.id);
      socket.on("event:message", async ({ message }: { message: string }) => {
        console.log("New Message Rec.", message);
        // publish this message to redis
        await pub.publish("MESSAGES", JSON.stringify({ message }));
      });
    });
    sub.on('message', (channel, message) => {
      io.emit("message", message);
    })
  }

  get io() {
    return this._io;
  }
}

export default SocketService;