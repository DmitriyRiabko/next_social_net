import Chat from "@/components/screens/chats/Chat";
import ChatsList from "@/components/screens/chats/ChatsList";
import CurrentUser from "@/components/screens/chats/CurrentUser";


export default function ChatPage() {
  return (
    <div
    className="grid h-full" style={
      {
        gridTemplateColumns:'.7fr 3fr'
      }
    }>
      <div className="border-r border-border">
        <CurrentUser/>
        <ChatsList/>

      </div>
      <div>
        <Chat/>
      </div>
    </div>
  );
}
