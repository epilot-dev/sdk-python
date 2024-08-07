"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .address import Address, AddressTypedDict, EmailType, SendError, SendErrorTypedDict, SendStatus
from .assignthreadop import AssignThreadRequest, AssignThreadRequestTypedDict, RequestBody, RequestBodyTypedDict
from .assignusersop import AssignUsersRequest, AssignUsersRequestBody, AssignUsersRequestBodyTypedDict, AssignUsersRequestTypedDict
from .attachmentsrelation import AttachmentsRelation, AttachmentsRelationTypedDict
from .createdraftop import CreateDraftResponseBody, CreateDraftResponseBodyTypedDict, CreateDraftSendStatus, CreateDraftType
from .deletemessageop import DeleteMessageRequest, DeleteMessageRequestTypedDict
from .deletethreadop import DeleteThreadRequest, DeleteThreadRequestTypedDict
from .file import File, FileTypedDict
from .generatesuggestedreplyop import GenerateSuggestedReplyRequest, GenerateSuggestedReplyRequestTypedDict, GenerateSuggestedReplyResponseBody, GenerateSuggestedReplyResponseBodyTypedDict, GenerateSuggestedReplyStatus, GenerateSuggestedReplyType, Payload, PayloadTypedDict
from .getgenaifeedbackop import GetGenAIFeedbackRequest, GetGenAIFeedbackRequestTypedDict, GetGenAIFeedbackResponseBody, GetGenAIFeedbackResponseBodyTypedDict, GetGenAIFeedbackResults, GetGenAIFeedbackResultsTypedDict, GetGenAIFeedbackType
from .getinfoop import GetInfoGenAIPayload, GetInfoGenAIPayloadTypedDict, GetInfoGenAIResponseBody, GetInfoGenAIResponseBodyTypedDict, GetInfoGenAIStatus, GetInfoGenAIType, GetInfoPayload, GetInfoPayloadTypedDict, GetInfoRequest, GetInfoRequestTypedDict, GetInfoResponse, GetInfoResponseBody, GetInfoResponseBodyTypedDict, GetInfoResponseTypedDict, GetInfoStatus, GetInfoType
from .getmessageop import GetMessageRequest, GetMessageRequestTypedDict, GetMessageResponse, GetMessageResponseBody, GetMessageResponseBodyTypedDict, GetMessageResponseTypedDict, GetMessageSendStatus, GetMessageType
from .getmessagev2op import GetMessageV2Request, GetMessageV2RequestTypedDict
from .markreadmessageop import MarkReadMessageRequest, MarkReadMessageRequestTypedDict
from .markreadthreadop import MarkReadThreadRequest, MarkReadThreadRequestTypedDict
from .markunreadmessageop import MarkUnreadMessageRequest, MarkUnreadMessageRequestTypedDict
from .markunreadthreadop import MarkUnreadThreadRequest, MarkUnreadThreadRequestTypedDict
from .message import Message, MessageSendStatus, MessageTypedDict, Type
from .messagerequestparams import MessageRequestParams, MessageRequestParamsTypedDict, Thread, ThreadTypedDict
from .messagev2 import MessageV2, MessageV2SendStatus, MessageV2Type, MessageV2TypedDict
from .patchinfoop import PatchInfoGenAIResponseBody, PatchInfoGenAIResponseBodyData, PatchInfoPayload, PatchInfoPayloadTypedDict, PatchInfoRequest, PatchInfoRequestBody, PatchInfoRequestBodyTypedDict, PatchInfoRequestTypedDict, PatchInfoResponseBody, PatchInfoResponseBodyTypedDict, PatchInfoStatus, PatchInfoType, Status
from .sdkerror import SDKError
from .searchparams import SearchParams, SearchParamsTypedDict
from .searchthreadsop import Results, ResultsTypedDict, SearchThreadsResponseBody, SearchThreadsResponseBodyTypedDict
from .security import Security, SecurityTypedDict
from .senddraftop import SendDraftResponseBody, SendDraftResponseBodyTypedDict, SendDraftSendStatus, SendDraftType
from .sendmessageop import SendMessageRequest, SendMessageRequestTypedDict
from .trashmessageop import TrashMessageRequest, TrashMessageRequestTypedDict
from .trashthreadop import TrashThreadRequest, TrashThreadRequestTypedDict
from .untrashmessageop import UntrashMessageRequest, UntrashMessageRequestTypedDict
from .untrashthreadop import UntrashThreadRequest, UntrashThreadRequestTypedDict
from .updatemessageop import UpdateMessageResponseBody, UpdateMessageResponseBodyTypedDict, UpdateMessageSendStatus, UpdateMessageType
from .updatethreadop import UpdateThreadResponseBody, UpdateThreadResponseBodyTypedDict

__all__ = ["Address", "AddressTypedDict", "AssignThreadRequest", "AssignThreadRequestTypedDict", "AssignUsersRequest", "AssignUsersRequestBody", "AssignUsersRequestBodyTypedDict", "AssignUsersRequestTypedDict", "AttachmentsRelation", "AttachmentsRelationTypedDict", "CreateDraftResponseBody", "CreateDraftResponseBodyTypedDict", "CreateDraftSendStatus", "CreateDraftType", "DeleteMessageRequest", "DeleteMessageRequestTypedDict", "DeleteThreadRequest", "DeleteThreadRequestTypedDict", "EmailType", "File", "FileTypedDict", "GenerateSuggestedReplyRequest", "GenerateSuggestedReplyRequestTypedDict", "GenerateSuggestedReplyResponseBody", "GenerateSuggestedReplyResponseBodyTypedDict", "GenerateSuggestedReplyStatus", "GenerateSuggestedReplyType", "GetGenAIFeedbackRequest", "GetGenAIFeedbackRequestTypedDict", "GetGenAIFeedbackResponseBody", "GetGenAIFeedbackResponseBodyTypedDict", "GetGenAIFeedbackResults", "GetGenAIFeedbackResultsTypedDict", "GetGenAIFeedbackType", "GetInfoGenAIPayload", "GetInfoGenAIPayloadTypedDict", "GetInfoGenAIResponseBody", "GetInfoGenAIResponseBodyTypedDict", "GetInfoGenAIStatus", "GetInfoGenAIType", "GetInfoPayload", "GetInfoPayloadTypedDict", "GetInfoRequest", "GetInfoRequestTypedDict", "GetInfoResponse", "GetInfoResponseBody", "GetInfoResponseBodyTypedDict", "GetInfoResponseTypedDict", "GetInfoStatus", "GetInfoType", "GetMessageRequest", "GetMessageRequestTypedDict", "GetMessageResponse", "GetMessageResponseBody", "GetMessageResponseBodyTypedDict", "GetMessageResponseTypedDict", "GetMessageSendStatus", "GetMessageType", "GetMessageV2Request", "GetMessageV2RequestTypedDict", "MarkReadMessageRequest", "MarkReadMessageRequestTypedDict", "MarkReadThreadRequest", "MarkReadThreadRequestTypedDict", "MarkUnreadMessageRequest", "MarkUnreadMessageRequestTypedDict", "MarkUnreadThreadRequest", "MarkUnreadThreadRequestTypedDict", "Message", "MessageRequestParams", "MessageRequestParamsTypedDict", "MessageSendStatus", "MessageTypedDict", "MessageV2", "MessageV2SendStatus", "MessageV2Type", "MessageV2TypedDict", "PatchInfoGenAIResponseBody", "PatchInfoGenAIResponseBodyData", "PatchInfoPayload", "PatchInfoPayloadTypedDict", "PatchInfoRequest", "PatchInfoRequestBody", "PatchInfoRequestBodyTypedDict", "PatchInfoRequestTypedDict", "PatchInfoResponseBody", "PatchInfoResponseBodyTypedDict", "PatchInfoStatus", "PatchInfoType", "Payload", "PayloadTypedDict", "RequestBody", "RequestBodyTypedDict", "Results", "ResultsTypedDict", "SDKError", "SearchParams", "SearchParamsTypedDict", "SearchThreadsResponseBody", "SearchThreadsResponseBodyTypedDict", "Security", "SecurityTypedDict", "SendDraftResponseBody", "SendDraftResponseBodyTypedDict", "SendDraftSendStatus", "SendDraftType", "SendError", "SendErrorTypedDict", "SendMessageRequest", "SendMessageRequestTypedDict", "SendStatus", "Status", "Thread", "ThreadTypedDict", "TrashMessageRequest", "TrashMessageRequestTypedDict", "TrashThreadRequest", "TrashThreadRequestTypedDict", "Type", "UntrashMessageRequest", "UntrashMessageRequestTypedDict", "UntrashThreadRequest", "UntrashThreadRequestTypedDict", "UpdateMessageResponseBody", "UpdateMessageResponseBodyTypedDict", "UpdateMessageSendStatus", "UpdateMessageType", "UpdateThreadResponseBody", "UpdateThreadResponseBodyTypedDict"]
